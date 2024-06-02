<?php

namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;

class SearchController extends AbstractController
{
    #[Route('/', name: 'app_search')]
    public function index(): Response
    {
        return $this->render('index.html.twig', [
            'controller_name' => 'SearchController',
        ]);
    }

    #[Route('/search', name: 'search', methods: ['GET'])]
    public function search(Request $request): JsonResponse
    {
        $searchTerm = $request->query->get('searchTerm');

        // Lecture du fichier data.json
        $jsonData = file_get_contents('data.json');
        $dataArray = json_decode($jsonData, true);

        // Recherche dans les données
        $results = [];
        foreach ($dataArray as $data) {
            // Recherche par nom, prénom ou e-mail
            if (str_contains(strtolower($data['nom']), strtolower($searchTerm)) ||
                str_contains(strtolower($data['prenom']), strtolower($searchTerm)) ||
                str_contains(strtolower($data['email'][0]), strtolower($searchTerm))) {
                $results[] = $data;
            }
        }

        return new JsonResponse($results);
    }
}
